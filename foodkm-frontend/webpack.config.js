const HtmlWebPackPlugin = require("html-webpack-plugin");
const CopyWebpackPlugin = require('copy-webpack-plugin');

const htmlPlugin = new HtmlWebPackPlugin({
  template: "./src/index.html",
  filename: "./index.html"
});


const copyConfig = new CopyWebpackPlugin([{
  from: './src/production.js',
  to: './config.js',
  toType: 'file'
}])


module.exports = {
    entry: "./src/index.jsx",
    output: {
      filename: "bundle.js",
      path: __dirname + "/dist"
    },

    mode: "development",

    // Enable sourcemaps for debugging webpack"s output.

    resolve: {
      // Add ".ts" and ".tsx" as resolvable extensions.
      extensions: [".ts", ".tsx", ".js", ".json", ".jsx"]
    },

    plugins: [htmlPlugin, copyConfig],

    module: {
      rules: [
        {
          test: /\.jsx$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader",
            options: {
              babelrc: false,
              presets: ["@babel/preset-env", "@babel/preset-react"]
            }
          }
        },
        {
          test: /\.css$/,
          use: ["style-loader", "css-loader"]
        },
        {
            test: /\.(woff|woff2|eot|ttf|svg|gif)$/,
            loader: 'url-loader?limit=1000000'
        },
        {
            test: /\.(jpeg|png|jpg)$/,
            use: [
                {
                    loader: 'file-loader',
                    options: {
                        name: '[path][name].[ext]',
                    }
                }
            ]
        },
      ]
    },

  };
