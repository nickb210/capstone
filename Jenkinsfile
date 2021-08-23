pipeline {
    agent any
    
    stages {

        stage('Stop and remove docker container and image') {
            steps {
                echo "**********************************************"
                echo "              PULL NEW IMG"
                echo "**********************************************"

                sh "chmod 400 ${env.PRIVATE_KEY}"

                dir ('/Users/nicholausbrell/Desktop/capstone/deploy/') {
                    sh "${env.TERRAFORM_HOME}/terraform output instance_aws_eip > ec2_ip"

                    //sh "cat ec2_ip"

                    sh ("""sed -i -e "s/\\./-/g" ec2_ip""")
                    sh ("""sed -i -e "s/\\"//g" ec2_ip""")

                    // Script to set EC2 instance ip address to Jenkinsfile environment variable
                    //script {
                    //    env.EC2_IP = readFile('ec2_ip').trim()
                    //}

                    // save EC2 instance IP address to variable env.EC2_IP
                    // save docker image ID to variable env.DOCKER_IMG_ID
                    // save docker container ID to variable env.DOCKER_CONTAINER_ID
                    script {
                        env.EC2_IP = readFile('ec2_ip').trim()

                        env.DOCKER_IMG_ID = sh (
                            script: "ssh -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker image ls -aq\"",
                            returnStdout: true
                        ).trim()

                        env.DOCKER_CONTAINER_ID = sh (
                            script: "ssh -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker container ls -aq\"",
                            returnStdout: true
                        ).trim()
                    }

                    echo "EC2_IP              = ${env.EC2_IP}"
                    echo "DOCKER_IMG_ID       = ${env.DOCKER_IMG_ID}"
                    echo "DOCKER_CONTAINER_ID = ${env.DOCKER_CONTAINER_ID}"

                    //sh "ssh -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker container stop ${env.DOCKER_CONTAINER_ID}\" "
                    //sh "ssh -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker container rm ${env.DOCKER_CONTAINER_ID}\" "
                    
                    // remove docker image
                    //sh "ssh -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker image rm ${env.DOCKER_IMG_ID}\" "

                    //sh """ssh -i ${env.PRIVATE_KEY} ec2-user@ec2-52-202-178-179.compute-1.amazonaws.com \"sudo docker pull nickb09/capstone:latest\" """
                    //sh """ssh -i ${env.PRIVATE_KEY} ec2-user@ec2-52-202-178-179.compute-1.amazonaws.com \"sudo docker pull nickb09/capstone:latest\" """
                    //sh """ssh -i ${env.PRIVATE_KEY} ec2-user@ec2-52-202-178-179.compute-1.amazonaws.com \"sudo docker run -p 80:80 nickb09/capstone:latest\" """
                    
                }
            }
        }

    }
}