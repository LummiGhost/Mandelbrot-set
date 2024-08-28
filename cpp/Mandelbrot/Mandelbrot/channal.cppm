

module canvas;

import std;

template<typename T>
class Channal {
	using Shape = std::pair<size_t, size_t>;

protected:
	std::vector<T> data;
	Shape shape;

	constexpr size_t __SIMD_SIZE = 4;

public:
	Channal() = default;
	Channal(const Channal&) = default;
	Channal(Channal&&) = default;

	Channal(Shape _shape):
		data(shape.first* shape.second),
		shape(_shape)
	{}
	Channal(size_t width, size_t height) :
		data(width* height),
		shape(width, height)
	{}

	Channal& operator=(const Channal&) = default;
	Channal& operator=(Channal&&) = default;

public:
	std::vector<T> flatten() const {
		return data;
	}
	std::vector<std::vector<T>> raw() const{
		std::vector<std::vector<T>> raw;
		for (size_t i = 0; i < shape().first; i++) {
			std::vector<T> row;
			for (size_t j = 0; j < shape().second; j++) {
				row.push_back((*this)(i, j));
			}
			raw.push_back(row);
		}
		return raw;
	}
	Channal reshape(Shape shape) const {
		Channal channal(shape);
		/*for (size_t i = 0; i < shape.first; i++) {
			for (size_t j = 0; j < shape.second; j++) {
				channal(i, j) = (*this)(i, j);
			}
		}*/
		return channal;
	}

	Channal map(std::function<T(T)> f) const {
		Channal channal(shape);
		for (size_t i = 0; i < shape.first; i++) {
			for (size_t j = 0; j < shape.second; j++) {
				channal(i, j) = f((*this)(i, j));
			}
		}
		return std::move(channal);
	}

	Channal& process(std::function<T(T)> f) {
		for (size_t i = 0; i < shape.first; i++) {
			for (size_t j = 0; j < shape.second; j++) {
				(*this)(i, j) = f((*this)(i, j));
			}
		}
		return *this;
	}

	Channal& set(Shape shape, std::vector<T> data) {
		this->shape = shape;
		this->data = data;
		return *this;
	}

	Channal& reset(T value = T()) {
		/*for (size_t i = 0; i < shape.first; i++) {
			for (size_t j = 0; j < shape.second; j++) {
				(*this)(i, j) = value;
			}
		}*/
		std::fill(data.begin(), data.end(), value);
		return *this;
	}

public:

	static Channal Zeros(Shape shape) {
		Channal channal(shape);
		channal.reset(0);
		return std::move(channal);
	}

	static Channal Ones(Shape shape) {
		Channal channal(shape);
		channal.reset(1);
		return std::move(channal);
	}

	static Channal Max(Shape shape) {
		Channal channal(shape);
		channal.reset(std::numeric_limits<T>::max());
		return std::move(channal);
	}

	static Channal Identity(Shape shape) {
		Channal channal(shape);
		for (size_t i = 0; i < shape.first; i++) {
			for (size_t j = 0; j < shape.second; j++) {
				if (i == j) {
					channal(i, j) = 1;
				}
				else {
					channal(i, j) = 0;
				}
			}
		}
		return std::move(channal);
	}
};