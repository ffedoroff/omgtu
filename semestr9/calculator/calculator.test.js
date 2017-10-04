const calculate = require('./calculator');

test('adds 1+2 to equal 3', () => {
  expect(calculate("1+2")).toBe(3);
});

test('adds 1.1+2.1 to equal 3.2', () => {
  expect(calculate("1.1+2.1")).toBe(3.2);
});

test('adds 7.1-2 to equal 5.1', () => {
  expect(calculate("7.1-2")).toBe(5.1);
});

test('adds 7.1-2- to equal 5.1', () => {
  expect(calculate("7.1-2-")).toBe(5.1);
});

test('adds 7.1÷2 to equal 3.55', () => {
  expect(calculate("7.1÷2")).toBe(3.55);
});

test('adds 7.1*2 to equal 14.2', () => {
  expect(calculate("7.1*2")).toBe(14.2);
});
