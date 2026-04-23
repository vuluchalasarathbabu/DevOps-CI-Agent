pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Add build steps here if necessary
            }
        }
    }

    post {
        always {
            echo 'Sending logs to FastAPI receiver...'
            script {
                def payload = [
                    buildNumber: env.BUILD_NUMBER,
                    jobName: env.JOB_NAME,
                    status: currentBuild.currentResult,
                    consoleLog: currentBuild.rawBuild.getLog(1000) // last 1000 lines
                ]
                def jsonPayload = groovy.json.JsonOutput.toJson(payload)

                // Send HTTP POST to FastAPI
                def response = httpRequest(
                    httpMode: 'POST',
                    contentType: 'APPLICATION_JSON',
                    requestBody: jsonPayload,
                    url: 'http://localhost:8000/jenkins-webhook'
                )
                echo "Webhook response: ${response.status}"
            }
        }
    }
}


