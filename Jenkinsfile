pipeline {
    agent any
    stages {
	stage('Checkout') {
	    steps {
		checkout scm
	    }
	}
        stage('Build') {
            steps {
                echo 'Hello Jenkins! This is the build stage.'
            }
        }
        stage('Run Python script') {
            steps {
                echo 'Running tests...'
		sh 'python main.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to production...'
            }
        }
    }
}
