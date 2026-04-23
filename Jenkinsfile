import groovy.json.JsonOutput
import java.net.URL
import java.net.HttpURLConnection

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''
                    echo Building the application... > build.log
                '''
            }
        }
    }

    post {
        always {
            script {
                def logContent = readFile('build.log')
                def payload = [
                    buildNumber: env.BUILD_NUMBER,
                    jobName: env.JOB_NAME,
                    status: currentBuild.currentResult,
                    consoleLog: logContent
                ]
                def jsonPayload = JsonOutput.toJson(payload)

                // Send POST request without plugin or approval
                def url = new URL("http://localhost:8000/jenkins-webhook")
                def conn = (HttpURLConnection) url.openConnection()
                conn.setRequestMethod("POST")
                conn.setRequestProperty("Content-Type", "application/json")
                conn.doOutput = true
                conn.outputStream.write(jsonPayload.getBytes("UTF-8"))
                conn.outputStream.flush()
                conn.outputStream.close()

                echo "Webhook response code: ${conn.responseCode}"
            }
        }
    }
}
