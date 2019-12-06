
describe('day 1, part 1', () => {
  test.each`
    input | expected
    ${1}  | ${1}
  `('$input is $expected', ({ input, expected }) => {
    expect(input).toBe(expected);
  });
});
