pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'npm install typescript'
                sh 'npm install cypress --save-dev'
                sh 'npm run cypress:run'
            }
        }
    }
}
