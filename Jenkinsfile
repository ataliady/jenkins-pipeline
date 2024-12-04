pipeline {
    agent any
    stages {
	stage('Checkout') {
	    steps {
		git 'https://github.com/ataliady/jenkins-pipeline.git'
	    }
	}
        stage('Build') {
            steps {
                echo 'Hello Jenkins! This is the build stage.'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to production...'
            }
        }
    }
}
