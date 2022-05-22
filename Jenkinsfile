pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh """
                    pwd
                    ls -altr
                """
            }
        }
        stage('Build') {
            steps {
                sh """
                    python -m venv ./venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                """
            }
        }
        stage('Test') {
            steps {
                sh "python -m pytest -v"
            }
        }
        stage('Deploy') {
            steps {
                sh "echo 'deploying....'"
            }
        }
    }
}