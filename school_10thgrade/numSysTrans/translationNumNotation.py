from decimal import Decimal

RADIX_NUMS = {str(n): n for n in range(10)} | {chr(i + 55): i for i in range(10, 36)}


def is_int(num: str) -> bool:
    if len(num.split(',')) == 1:
        return True
    return False


def define_positions(num: str) -> list[int]:
    int_part = [i for i in range(len(num.split(',')[0]) - 1, -1, -1)]
    if is_int(num):
        return int_part
    return int_part + [-i - 1 for i in range(len(num.split(',')[1]))]


def to_decimal(num: str, source_radix: int) -> str:
    res = Decimal(0)
    positions = define_positions(num)
    p_index = 0
    for i in ''.join(num.split(',')):
        res += Decimal(RADIX_NUMS[i] * source_radix ** Decimal(positions[p_index]))
        p_index += 1
    return ','.join(str(res).split('.'))


def from_decimal(num: str, required_radix: int, round_index) -> str:
    fractional_res = []
    if not is_int(num):
        _num = num.split(',')
        fractional_part = int(_num[1]) * 10 ** Decimal(-len(_num[1]))
        for i in range(round_index + 1):
            fractional_part *= required_radix
            req_num = list(RADIX_NUMS.keys())[
                list(RADIX_NUMS.values()).index(int(fractional_part))
            ]
            fractional_res.append(req_num)
            if fractional_part >= 1:
                fractional_part %= 1

    int_part = int(num.split(',')[0])
    int_res = []

    while int_part != 0:
        req_num = list(RADIX_NUMS.keys())[
            list(RADIX_NUMS.values()).index(divmod(int_part, required_radix)[1])
        ]
        int_res.append(req_num)
        int_part = divmod(int_part, required_radix)[0]
    if fractional_res:
        return ''.join(int_res[::-1]) + ',' + ''.join(fractional_res)
    return ''.join(int_res[::-1])


def _round(num: str, source_radix: int, round_idx) -> str:
    if is_int(num):
        return num
    num_fract = num.split(',')[1]
    try:
        num_fract[round_idx]
    except IndexError:
        return num
    rounding_threshold = source_radix // 2
    if RADIX_NUMS[num_fract[round_idx]] >= rounding_threshold:
        return (
            num.split(',')[0]
            + ','
            + num_fract[: round_idx - 1]
            + list(RADIX_NUMS.keys())[
                list(RADIX_NUMS.values()).index(
                    RADIX_NUMS[num_fract[round_idx - 1]] + 1
                )
            ]
        )
    else:
        return num.split(',')[0] + ',' + num_fract[:round_idx]


with open(
    r'C:\Users\vysok\Desktop\Python tasks\school_10thgrade\numSysTrans\input.txt', 'tr'
) as f:
    for i in f.readlines():
        i = i.split()
        round_idx = int(i[3])
        res = []
        res.append(
            _round(
                from_decimal(to_decimal(i[0], int(i[1])), int(i[2]), round_idx),
                int(i[2]),
                round_idx,
            )
        )

with open(
    r'C:\Users\vysok\Desktop\Python tasks\school_10thgrade\numSysTrans\output.txt', 'tw'
) as f:
    f.writelines(res)
