pipeline {
    agent any

    tool name: 'Terraform', type: 'terraform'
    
    parameters {
        string(name: 'environment', defaultValue: 'default', description: 'Workspace/environment file to use for deployment')
        string(name: 'version', defaultValue: '', description: 'Version variable to pass to Terraform')
        booleanParam(name: 'autoApprove', defaultValue: false, description: 'Automatically run apply after generating plan?')
    }
    
    environment {
        AWS_ACCESS_KEY_ID     = credentials('ASIAYCEGTPYPXFULZSOV')
        AWS_SECRET_ACCESS_KEY = 'LyMV3IaTZ2tFlSbwg4zLYLmW4Nazke1qAR8QPOLw'
        TF_IN_AUTOMATION      = '1'
    }

    stages {
        stage('Plan') {
            steps {
                script {
                    currentBuild.displayName = params.version
                }
                sh 'echo $AWS_ACCESS_KEY_ID'
                sh 'echo $AWS_SECRET_ACCESS_KEY'
                sh 'terraform init -input=false'
                sh "terraform plan -input=false "
            }
        }


    }

    post {
        always {
            sh 'echo "*******************"'
            sh 'BUILD COMPLETE'
            sh 'echo "*******************"'
        }
    }
}