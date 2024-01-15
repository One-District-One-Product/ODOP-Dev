// math.test.js
const add = require('../src/math'); // Import the function you want to test

describe('add function', () => {
  it('should add two numbers correctly', () => {
    // Arrange: Set up the initial conditions
    const a = 5;
    const b = 3;

    // Act: Call the function
    const result = add(a, b);

    // Assert: Check the result
    expect(result).toBe(8);
  });

  it('should handle negative numbers', () => {
    const a = -5;
    const b = 3;
    const result = add(a, b);
    expect(result).toBe(-2);
  });
});