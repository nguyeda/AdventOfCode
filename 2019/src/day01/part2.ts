import { add, compose, map, reduce, tail, unfold } from 'ramda';
import { readLines } from '../_utils';

import { computeFuelForMass } from './part1';

export const computeTotalFuelForMass: (mass: number) => number = compose(
  reduce<number, number>(add, 0),
  tail,
  unfold((m: number) => m <= 0 ? false : [m, computeFuelForMass(m)]),
);

export const computeFuelForMasses: (masses: number[]) => number = compose(
  reduce<number, number>(add, 0),
  map(computeTotalFuelForMass),
);

const computeFuelForMassesFromFile: (path: string) => number = compose(
  computeFuelForMasses,
  map(it => +it),
  readLines,
);

export default computeFuelForMassesFromFile;
