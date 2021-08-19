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
                echo "              LS + PWD"
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
        stage('Terraform init') {
            steps {
                echo "**********************************************"
                echo "              TERRAFORM INIT"
                echo "**********************************************"
                sh "${env.TERRAFORM_HOME}/terraform -chdir=deploy/ init"
            }
        }
        
        stage('Terraform plan') {
            steps {
                echo "**********************************************"
                echo "              TERRAFORM PLAN"
                echo "**********************************************"
                sh "${env.TERRAFORM_HOME}/terraform -chdir=deploy/ plan"
            }
        }
    }
}