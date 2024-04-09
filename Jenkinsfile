pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/saiprabhu-dandanayak/jenkins.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/saiprabhu-dandanayak/jenkins.git'
                sh 'python3 main.py'
            }
        }
        
    }
} 
