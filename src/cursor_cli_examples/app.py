"""Flask web application for calculator UI."""

from flask import Flask, render_template, request, jsonify
from cursor_cli_examples.main import add, subtract, multiply, divide, power, Chain

app = Flask(__name__)


@app.route('/')
def calculator():
    """Render the calculator page."""
    return render_template('calculator.html')


@app.route('/api/calculate', methods=['POST'])
def calculate():
    """Handle calculation requests."""
    try:
        data = request.get_json()
        operation = data.get('operation')
        left = float(data.get('left', 0))
        right = float(data.get('right', 0))
        
        # Convert to int if they're whole numbers for operations that expect ints
        if left.is_integer():
            left = int(left)
        if right.is_integer():
            right = int(right)
        
        result = None
        
        if operation == 'add':
            result = add(left, right)
        elif operation == 'subtract':
            result = subtract(left, right)
        elif operation == 'multiply':
            result = multiply(left, right)
        elif operation == 'divide':
            if right == 0:
                return jsonify({'error': 'Division by zero'}), 400
            result = divide(left, right)
        elif operation == 'power':
            if not isinstance(right, int) or right < 0:
                return jsonify({'error': 'Exponent must be a non-negative integer'}), 400
            result = power(left, right)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({'result': result})
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except ZeroDivisionError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred during calculation'}), 500


@app.route('/api/chain', methods=['POST'])
def chain_calculate():
    """Handle chain calculation requests."""
    try:
        data = request.get_json()
        initial_value = float(data.get('initial', 0))
        operations = data.get('operations', [])
        
        if initial_value.is_integer():
            initial_value = int(initial_value)
        
        chain = Chain(initial_value)
        
        for op in operations:
            operation = op.get('operation')
            value = float(op.get('value', 0))
            
            if value.is_integer() and operation != 'divide':
                value = int(value)
            
            if operation == 'add':
                chain = chain.add(value)
            elif operation == 'subtract':
                chain = chain.subtract(value)
            elif operation == 'multiply':
                chain = chain.multiply(value)
            elif operation == 'divide':
                if value == 0:
                    return jsonify({'error': 'Division by zero'}), 400
                chain = chain.divide(value)
            elif operation == 'power':
                if not isinstance(value, int) or value < 0:
                    return jsonify({'error': 'Exponent must be a non-negative integer'}), 400
                chain = chain.power(value)
            else:
                return jsonify({'error': f'Invalid operation: {operation}'}), 400
        
        return jsonify({'result': chain.value()})
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except ZeroDivisionError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred during calculation'}), 500


def main():
    """Main entry point for the calculator web application."""
    print("🧮 Starting Calculator Web UI...")
    print("📱 Open your browser to: http://localhost:5001")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5001)


if __name__ == '__main__':
    main()
