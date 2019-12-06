import { computeFuelForMasses, computeTotalFuelForMass } from './part2';

describe('day 1, part 2', () => {
  test.each`
    mass      | expected
    ${0}      | ${0}
    ${12}     | ${2}
    ${14}     | ${2}
    ${1969}   | ${966}
    ${100756} | ${50346}
  `('fuel for $mass is $expected', ({ mass, expected }) => {
    expect(computeTotalFuelForMass(mass)).toBe(expected);
  });

  test('fuel for masses adds up', () => {
    expect(computeFuelForMasses([12, 14, 1969, 100756])).toBe(2 + 2 + 966 + 50346);
  });
});
