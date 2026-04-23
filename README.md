# Jenkins Hello World Project

This project is a simple Node.js application that demonstrates a "Hello World" functionality. It includes a function that returns the string "Hello, World!" and is accompanied by unit tests to verify its correctness.

## Project Structure

```
jenkins-hello-world
├── src
│   └── app.js          # Contains the Hello World function
├── test
│   └── app.test.js     # Contains unit tests for the Hello World function
├── Jenkinsfile         # CI/CD pipeline configuration for Jenkins
├── package.json        # npm configuration file
├── .gitignore          # Files and directories to be ignored by Git
└── README.md           # Project documentation
```

## Getting Started

To set up and run the application, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd jenkins-hello-world
   ```

2. **Install dependencies**:
   ```
   npm install
   ```

3. **Run the application**:
   ```
   node src/app.js
   ```

4. **Run tests**:
   ```
   npm test
   ```

## Usage

The main function of the application is `sayHello`, which can be found in `src/app.js`. This function can be imported and used in other modules or tested directly.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.