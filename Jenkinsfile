pipeline {
    agent any
    
    stages {

        stage('Stop and remove docker container and image') {
            steps {
                echo "**********************************************"
                echo "              PULL NEW IMG"
                echo "**********************************************"

                sh "chmod 400 ${env.PRIVATE_KEY}"
                
                /*Ouput terraform variable (EC2 instances IP address) and save it locally to the file 'ec2_ip'*/
                dir ('/Users/nicholausbrell/Desktop/Critical Design + AVT/capstone/deploy/') {
                    sh "${env.TERRAFORM_HOME}/terraform output instance_aws_eip > ec2_ip"
                    
                    /*FILE ec2_ip: replace every '.' with a '-'
                    "1.2.3.4" -> 1-2-3-4
                    */
                    sh ("""sed -i -e "s/\\./-/g" ec2_ip""")

                    /*FILE ec2_ip: remove quotation marks*/
                    sh ("""sed -i -e "s/\\"//g" ec2_ip""")

                    /* 
                    * Save EC2 instance IP address to variable env.EC2_IP
                    * Save docker image ID to variable env.DOCKER_IMG_ID
                    * Save docker container ID to variable env.DOCKER_CONTAINER_ID
                    */
                    script {
                        env.EC2_IP = readFile('ec2_ip').trim()

                        env.DOCKER_IMG_ID = sh (
                            script: "ssh -o \"StrictHostKeyChecking no\" -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker image ls -aq\"",
                            returnStdout: true
                        ).trim()

                        env.DOCKER_CONTAINER_ID = sh (
                            script: "ssh -o \"StrictHostKeyChecking no\" -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker container ls -aq\"",
                            returnStdout: true
                        ).trim()
                    }

                    echo "EC2_IP              = ${env.EC2_IP}"
                    echo "DOCKER_IMG_ID       = ${env.DOCKER_IMG_ID}"
                    echo "DOCKER_CONTAINER_ID = ${env.DOCKER_CONTAINER_ID}"

                    // Stop and remove docker container
                    sh "ssh -o \"StrictHostKeyChecking no\" -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker container stop ${env.DOCKER_CONTAINER_ID}\" "
                    sh "ssh -o \"StrictHostKeyChecking no\" -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker container rm ${env.DOCKER_CONTAINER_ID}\" "
                    
                    // Remove docker image
                    sh "ssh -o \"StrictHostKeyChecking no\" -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker image rm ${env.DOCKER_IMG_ID}\" "

                    // pull new image from dockerhub, the run image just pulled
                    sh "ssh -o \"StrictHostKeyChecking no\" -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker pull nickb09/capstone\" "
                    sh "ssh -o \"StrictHostKeyChecking no\" -i ${env.PRIVATE_KEY} ec2-user@ec2-${env.EC2_IP}.compute-1.amazonaws.com \"sudo docker run -d -p 80:80 nickb09/capstone\" "
                    
                }
            }
        }
    }
}