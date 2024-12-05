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
		bat 'C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python312\\python.exe main.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to production...'
            }
        }
    }
}
