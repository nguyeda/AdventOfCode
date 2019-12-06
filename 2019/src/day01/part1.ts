import { __, add, compose, divide, map, max, reduce, subtract } from 'ramda';
import { readLines } from '../_utils';

export const computeFuelForMass: (mass: number) => number = compose(
  max<number>(0),
  subtract(__, 2),
  Math.floor,
  divide(__, 3),
);

export const computeFuelForMasses: (masses: number[]) => number = compose(
  reduce<number, number>(add, 0),
  map(computeFuelForMass),
);

const computeFuelForMassesFromFile: (path: string) => number = compose(
  computeFuelForMasses,
  map(it => +it),
  readLines,
);

export default computeFuelForMassesFromFile;
