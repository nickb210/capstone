pipeline {
    agent any
    
    stages {
//        stage('Checkout') {
//            steps {
//                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nickb210/capstone']]])
//            }
//        }
        stage('Test') {
            steps {
                echo "**********************************************"
                echo "              TEST"
                echo "**********************************************"
                sh "pwd"
                sh "ls -al"

                dir('deploy') {
                    sh "pwd"
                    sh "ls -al"
                }
                sh "pwd"
                sh "ls -al"
                sh "ls -alh ${env.PRIVATE_KEY}"

            }
        }

        stage('Pull new image') {
            steps {
                echo "**********************************************"
                echo "              TEST"
                echo "**********************************************"

                sh "chmod 400 ${env.PRIVATE_KEY}"
                sh "ssh -i ${env.PRIVATE_KEY} "

                
            }
        }

    }
}