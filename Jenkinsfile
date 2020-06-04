pipeline {

    environment {
        HOME="."

        GIT_URL = 'http://ec2-54-188-135-255.us-west-2.compute.amazonaws.com:30000/root/sample-cicd.git'
        GIT_BRANCH_NAME = "master"
        GIT_CREDENTIALS = "gitlab-key"
        CODE = git(branch: "${GIT_BRANCH_NAME}", credentialsId: "${GIT_CREDENTIALS}", url: "${GIT_URL}")

        DOCKER_IMAGE_TAG="python:3.7"

    }

    agent { label 'master'}


    stages('CI/CD pipeline'){


        stage ("run fuction test") {

            agent {
                docker {
                    image "${DOCKER_IMAGE_TAG}"
                    reuseNode true
                    //alwaysPull false
                }
            }

            steps ("run test file") {
                script {
                    sh "ls -l"
                    sh "python test.py"
                }
            }
        }

        stage ("docker build and push") {
            steps {
                
                script {

                    def file = readFile('VERSION')
                    def lines = file.readLines()
                    string versionString = lines[0]
                
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-key') {
                        

                        def registry = "zhenghongli/sample-webapp"

                        def customImage = docker.build(registry + ":$versionString")
                
                        /* Push the container to the custom Registry */
                        customImage.push()
                        
                        
                    }

                }

            }
        }
    }
}  