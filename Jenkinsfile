pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/saiprabhu-dandanayak/jenkins.git']]])
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/saiprabhu-dandanayak/jenkins.git'
                     // sh 'uvicorn main:app --reload'
                }
            }
        }   
    }
}
