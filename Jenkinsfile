
pipeline {
    agent any

    stages {
        stage('Checkout from GitHub') {
            steps {
                checkout scm
                echo 'Source code fetched successfully'
            }
        }

        stage('Run HTML Form Tests') {
            steps {
                bat 'py -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }
        failure {
            echo 'FAILURE: Check the test output for errors.'
        }
    }
}
