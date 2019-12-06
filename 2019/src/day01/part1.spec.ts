import { computeFuelForMass, computeFuelForMasses } from './part1';

describe('day 1, part 1', () => {
  test.each`
    mass      | expected
    ${12}     | ${2}
    ${14}     | ${2}
    ${1969}   | ${654}
    ${100756} | ${33583}
  `('fuel for $mass is $expected', ({ mass, expected }) => {
    expect(computeFuelForMass(mass)).toBe(expected);
  });

  test('fuel for masses adds up', () => {
    expect(computeFuelForMasses([12, 14, 1969, 100756])).toBe(2 + 2 + 654 + 33583);
  });
});
