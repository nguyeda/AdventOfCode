import fs from 'fs';

export const readLines = (path: string): string[] => fs
  .readFileSync(path, 'utf-8')
  .split(/\r?\n/)
  .map(it => it?.trim())
  .filter(it => !!it);
