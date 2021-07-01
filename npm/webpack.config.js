var webpack = require('webpack');
module.exports = {
  entry: {
    entry: __dirname + '/dist/index.js',
  },
  output: {
    path: __dirname  + '/dist/',
    filename: 'quoters.bundle.js',
    library: 'Quoters',
    libraryTarget: 'umd',
  },
  resolve: {
    fallback: { stream: require.resolve('stream-browserify') },
  },
  plugins: [
    new webpack.ProvidePlugin({
      process: 'process/browser',
      Buffer: ['buffer', 'Buffer'],
    }),
  ],
  mode: 'production',
};
