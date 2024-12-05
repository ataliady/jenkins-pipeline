pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Hello Jenkins! This is the build stage.'
            }
        }
	stage('Test Python') {
            steps {
                bat 'echo %PYTHON_HOME%'
                bat 'echo %PATH%'
                bat 'python --version'  // To confirm Python is recognized
            }
        }
        stage('Run Python script') {
            steps {
                echo 'Running tests...'
		bat 'python main.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to production...'
            }
        }
    }
}
