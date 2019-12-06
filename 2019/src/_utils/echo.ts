export const echo = (context?: string) => <T>(o: T): T => {
  console.log(context || '>', JSON.stringify(o));
  return o;
};
