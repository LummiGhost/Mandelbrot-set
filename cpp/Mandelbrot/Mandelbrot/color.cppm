module canvas;

import std;

namespace Color {
	enum class ColorSpace {
		RGB,
		RGBA,
		CMYK,
		YUV,
		YIQ,
		YCbCr,
		YPbPr,
	};

	namespace ColorVector {
		template<typename T>
		struct RGB {
			T r, g, b;

			RGB operator+(const RGB& other) const {
				return RGB{ r + other.r, g + other.g, b + other.b };
			}
			RGB operator-(const RGB& other) const {
				return RGB{ r - other.r, g - other.g, b - other.b };
			}

			operator RGBA<T>() const {
				return RGBA<T>{r, g, b, 0};
			}

		};
		
		template<typename T>
		struct RGBA {
			T r, g, b, a;

			RGBA operator+(const RGBA& other) const {
				return RGBA{ r + other.r, g + other.g, b + other.b, a + other.a };
			}
			RGBA operator-(const RGBA& other) const {
				return RGBA{ r - other.r, g - other.g, b - other.b, a - other.a };
			}

			operator RGB<T>() const {
				return RGB<T>{ r, g, b };
			}
			
		};

		template<typename T>
		struct CMYK {
			T c, m, y, k;

			CMYK operator+(const CMYK& other) const {
				return CMYK{ c + other.c, m + other.m, y + other.y, k + other.k };
			}
			CMYK operator-(const CMYK& other) const {
				return CMYK{ c - other.c, m - other.m, y - other.y, k - other.k };
			}
		};
	}

	class ColorSpaceConverter {
	public:
		template <typename T>
		static ColorVector::CMYK<T> RGB2CMYK(const ColorVector::RGB<T>& rgb) {
			T max_v = std::numeric_limits<T>::max();
			T k = max_v - std::max({ r, g, b };
			return ColorVector::CMYK<T>{
				(max_v - r - k) / (max_v - k),
				(max_v - g - k) / (max_v - k),
				(max_v - b - k) / (max_v - k),
				k)
			};
		}

		template <typename T>
		static ColorVector::RGB<T> CMYK2RGB(const ColorVector::CMYK<T>& cmyk) {
			T max_v = std::numeric_limits<T>::max();
			return ColorVector::RGB<T>{
				(max_v - c)* (max_v - k),
				(max_v - m)* (max_v - k),
				(max_v - y)* (max_v - k)
			};
		}

	};

}