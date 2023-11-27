pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/carpachecus/appserver-cred.git']])
            }
        }
    
        stage('test') {
            steps {
                 sh 'pytest test_launch.py'
            }
        }
        stage('Sonar Analysis') {
            environment {
                scannerHome = tool 'sonarqube5'
            }
            steps {
               withSonarQubeEnv('sonarqube') {
                   sh '''${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=carpachecus_appserver-cred \
                   -Dsonar.organization=carpachecus '''    
                }
            }
        }
        stage('Build and Push') {
            steps {
                script {
                        docker.withRegistry('docker-id') {

                        def dockerImage = docker.build("carpachecus/appserver-python:${env.BUILD_ID}")

                        dockerImage.push()

                    }
                }	
            }        
        }
    }   
}
