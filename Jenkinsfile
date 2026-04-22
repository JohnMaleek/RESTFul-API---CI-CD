pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'YOUR_DOCKERHUB_USERNAME/project1'
        GCP_REGION = 'us-central1'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/Project1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Test API') {
            steps {
                echo 'Testing the API...'
                sh 'docker run -d -p 5001:8080 --name test-api $DOCKER_IMAGE:latest'
                sh 'sleep 10'
                sh 'curl -f http://localhost:5001/users || exit 1'
                sh 'docker stop test-api'
                sh 'docker rm test-api'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing to Docker Hub...'
                sh 'docker login -u YOUR_DOCKERHUB_USERNAME -p YOUR_PASSWORD'
                sh 'docker push $DOCKER_IMAGE:latest'
            }
        }
    }
	stage('Deploy to Cloud Run') {
	    steps {
                echo 'Deploying to GCP Cloud RUN...'
                sh 'gcloud run deploy Project1 --image docker.io/myapi:latest --platform managed --region europe-west1 --allow-unauthenticated'
	    }

	 }
     }
}

