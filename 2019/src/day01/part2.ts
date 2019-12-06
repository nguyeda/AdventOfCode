import { __, add, compose, F, gt, ifElse, map, reduce, unfold } from 'ramda';
import { readLines } from '../_utils';

import { computeFuelForMass } from './part1';

export const computeTotalFuelForMass: (mass: number) => number = compose(
  reduce<number, number>(add, 0),
  unfold(ifElse(gt(__,0), compose(n => [n, n], computeFuelForMass), F))
);

export const computeFuelForMasses: (masses: number[]) => number = compose(
  reduce<number, number>(add, 0),
  map(computeTotalFuelForMass),
);

export const computeFuelForMassesFromFile: (path: string) => number = compose(
  computeFuelForMasses,
  map(it => +it),
  readLines,
);
