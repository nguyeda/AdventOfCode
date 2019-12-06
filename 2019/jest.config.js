module.exports = {
  moduleFileExtensions: ['ts', 'js', 'json'],

  testEnvironment: 'node',
  testRegex: '(/__test__/.*|(\\.|/)(e2e-)?(spec))\\.(jsx?|tsx?)$',
  testURL: 'http://localhost',

  transform: {
    '^.+\\.tsx?$': 'ts-jest',
  },
};
