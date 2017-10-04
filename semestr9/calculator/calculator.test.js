const sum2 = require('./calculator');

test('adds 1 + 2 to equal 3', () => {
  expect(sum2(1, 2)).toBe(3);
});