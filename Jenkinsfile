pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo '📦 Cloning repository...'
                git 'https://github.com/swaran05/ipl-score-predictor-final.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo '🐍 Setting up virtual environment...'
                bat '''
                if not exist venv (
                    C:\\Users\\win10\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m venv venv
                )
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo '🚀 Running the FastAPI app...'
                bat '''
                call venv\\Scripts\\activate
                python -m uvicorn src.model:app --host 0.0.0.0 --port 8000
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed. Check logs for details.'
        }
        success {
            echo '✅ Build completed successfully!'
        }
    }
}
