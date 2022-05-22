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
                    python3 -m venv ./venv
                    source venv/bin/activate
                    pip3 install -r requirements.txt
                    pip3 install pytest
                """
            }
        }
        stage('Test') {
            steps {
                sh "venv/bin/python3 -m pytest -v"
            }
        }
        stage('Deploy') {
            steps {
                sh "echo 'deploying....'"
            }
        }
    }
}