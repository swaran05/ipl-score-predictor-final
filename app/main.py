pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo '🐍 Setting up Python environment...'
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                echo '🤖 Training model and saving model.pkl...'
                bat '''
                call venv\\Scripts\\activate
                python train_model.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                bat '''
                call venv\\Scripts\\activate
                pytest > result.log
                type result.log
                '''
            }
        }

        stage('Run FastAPI App') {
            steps {
                echo '🚀 Starting FastAPI app in background...'
                bat '''
                call venv\\Scripts\\activate
                start /B uvicorn app.main:app --host 127.0.0.1 --port 8000 > server.log 2>&1
                timeout /t 10
                '''
            }
        }

        stage('Test API Endpoint') {
            steps {
                echo '🌐 Testing /predict endpoint...'
                bat '''
                call venv\\Scripts\\activate
                curl -X POST "http://127.0.0.1:8000/predict" ^
                -H "Content-Type: application/json" ^
                -d "{\\"overs\\":5,\\"wickets\\":1,\\"runs_so_far\\":45,\\"venue_factor\\":1}"
                '''
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up (stopping FastAPI server)...'
            bat 'taskkill /F /IM uvicorn.exe || exit 0'
        }

        success {
            echo '✅ Build and Test Successful!'
        }

        failure {
            echo '❌ Build Failed. Please check logs.'
        }
    }
}
