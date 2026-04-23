const { sayHello } = require('../src/app');

describe('sayHello function', () => {
    test('should return "Hello, World!"', () => {
        expect(sayHello()).toBe('Hello, World!');
    });
});