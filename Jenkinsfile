peline {
    agent any

    stages {
        stage('Hello') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/pinweitan/Room1']]])
            }
        
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/pinweitan/Room1'
                sh '''python3 ./summary/fizzbuzz.py > output
                   '''
            }
        }
    }
