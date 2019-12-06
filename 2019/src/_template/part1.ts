import { compose, identity } from 'ramda';
import { readLines } from '../_utils';

const fromFile: (path: string) => any = compose(
  identity,
  readLines,
);

export default fromFile;
