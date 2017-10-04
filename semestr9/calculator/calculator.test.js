const calculate = require('./calculator');

test('adds 1 + 2 to equal 3', () => {
  expect(calculate("1+2")).toBe(3);
});