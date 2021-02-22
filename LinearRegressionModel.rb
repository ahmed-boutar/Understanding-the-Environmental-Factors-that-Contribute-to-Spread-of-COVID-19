#Multivariable Linear Regression Learning Model
#Outputs model attribute weights

require 'matrix'
require 'csv'

class LinearRegression

  def initialize
    @mu = 0
    @sigma = 1
  end

  # Loads and normalizes the training data
  # xData: Two dimensiolnal array with the non-pivot attributes
  # yData: Array with the pivot attribute for each row of the data
  def loadData xData, yData
    # normalize the x data
    xData = normalize_data(xData)

    # add 1 column to our data
    xData = xData.map { |r| [1].concat(r) }

    @x = Matrix.rows( xData )
    @y = Matrix.rows( yData.collect { |e| [e] } )

    @theta = Matrix.zero(@x.column_count, 1)
  end

  # Mean Squared Error Computatons
  def findMSE test_x = nil, test_y = nil

    if not test_x.nil?
      test_x.each_index do |row|
        test_x[row].each_index do |i|
          test_x[row][i] = (test_x[row][i] - @mu[i]) / @sigma[i].to_f
        end
      end
      test_x = test_x.map { |r| [1].concat(r) }
    end

    # by default use training data to compute cost if no data is given
    cost_x = test_x.nil? ? @x : Matrix.rows( test_x )
    cost_y = test_y.nil? ? @y : Matrix.rows( test_y.collect { |e| [e] } )

    errors = ((cost_x * @theta) - cost_y)

    errors = errors.map { |e| (e.to_f**2)  }

    # Find the mean of the square errors
    mean_square_error = 0.5 * (errors.inject{ |sum, e| sum + e }.to_f / errors.row_size)

    return mean_square_error
  end

  # Calculate the optimal theta using the normal equation
  def trainData l = 0

    @lambda = l
    lambda_matrix = Matrix.build(@theta.row_size,@theta.row_size) do |c,r|
      (( c == 0 && r == 0) || c != r) ? 0 : 1;
    end

    # Calculate theta using the normal equation
    @theta = (@x.transpose * @x + @lambda * lambda_matrix ).inverse * @x.transpose * @y

    @theta.each do |q|
      puts q.abs()
    end

    return @theta
  end

  def normalize_data(xData, mu = nil, sigma = nil)

    row_size = xData.size
    column_count = xData[0].is_a?( Array) ? xData[0].size : 1

    x_norm = Array.new(row_size)
    @mu = Array.new(column_count)
    @sigma = Array.new(column_count)

    0.upto(column_count - 1) do |column|
      column_data = xData.map{ |e| e[column] }
      @mu[column] = column_data.inject{ |sum, e| sum + e } / row_size
      @sigma[column] = (column_data.max - column_data.min)
    end

    0.upto(row_size-1) do |row|
      row_data = xData[row]
      x_norm[row] = Array.new(column_count)
      row_data.each_index do |i|
        x_norm[row][i] = (row_data[i] - @mu[i]) / @sigma[i].to_f
      end
    end

    return x_norm

  end

end

xData = []
yData = []
pivotIndex = 0

CSV.foreach("allCountyDataNumOnly.csv", :headers => true) do |row| 
  count = 0
  xl = []
  row.each do |element|
    if count == pivotIndex
      yData.push(element[1].to_f)
    else
      xl.push(element[1].to_f)
    end
    count += 1
  end
  xData.push(xl)
end


# Create regression model
linear_regression = LinearRegression.new

# Load training data
linear_regression.loadData(xData, yData)

# Train the model
linear_regression.trainData

puts "Trained model with mse fit: #{linear_regression.findMSE}"
