
describe('day n, part 2', () => {
  test.each`
    input | expected
    ${1}  | ${1}
  `('$input is $expected', ({ input, expected }) => {
    expect(input).toBe(expected);
  });
});
