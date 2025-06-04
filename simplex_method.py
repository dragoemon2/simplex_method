from fractions import Fraction

Infinity = float('inf')

class Dictionary:
    def __init__(self, basis : list[int], unbasis : list[int], tableau : list[list[int]], use_fraction: bool = True):
        self.basis = basis # 基底変数
        self.unbasis = unbasis # 非基底変数
        self.tableau = tableau # 辞書
        if use_fraction:
            for i in range(len(self.tableau)):
                for j in range(len(self.tableau[i])):
                    self.tableau[i][j] = Fraction(self.tableau[i][j])
                    
    def simplex_method(self, print_progress: bool = True):
        """
        単体法を実行し、最適解を求める
        """
        while True:
            if print_progress:
                print(self.latex(), end=" \\\\\n")
            
            unbasis_cand = [(self.unbasis[j-1], j) for j in range(1, len(self.tableau[0])) if self.tableau[0][j] < 0]
            if len(unbasis_cand) == 0:
                return self.tableau[0][0], self.basis, self.unbasis, self.tableau
            else:
                _, j_pivot = min(unbasis_cand) # 候補のうち添字が最小の非基底を選択

            # ピボット列の選択
            min_ratio = Infinity
            basis_cand = []
            for i in range(1, len(self.tableau)):
                if self.tableau[i][j_pivot] < 0:
                    ratio = -self.tableau[i][0] / self.tableau[i][j_pivot]
                    if ratio < min_ratio:
                        min_ratio = ratio
                        basis_cand = [(self.basis[i-1], i)]
                    elif ratio == min_ratio:
                        basis_cand.append((self.basis[i-1], i))
            if len(basis_cand) == 0:
                raise ValueError("Unbounded solution")
            _, i_pivot = min(basis_cand) # 候補のうち添字が最小の基底を選択
            
            self.pivot(i_pivot, j_pivot)
            
    def pivot(self, i_pivot: int, j_pivot: int):
        # ピボット演算を行う
        i_pivot_column = self.tableau[i_pivot].copy()
        for i in range(len(self.tableau)):
            if i == i_pivot:
                factor = -1 / self.tableau[i_pivot][j_pivot]
                self.tableau[i] = [ factor * x for x in self.tableau[i] ]
                self.tableau[i][j_pivot] = -factor
            else: 
                factor = self.tableau[i][j_pivot] / i_pivot_column[j_pivot]
                self.tableau[i] = [ self.tableau[i][j] - factor * i_pivot_column[j] for j in range(len(self.tableau[i])) ]
                self.tableau[i][j_pivot] = factor
                
        # 基底変数と非基底変数の更新
        self.basis[i_pivot-1], self.unbasis[j_pivot-1] = self.unbasis[j_pivot-1], self.basis[i_pivot-1]
        
    def latex(self):
        """
        シンプレックス表をlatex形式で出力する
        """
        result = ""
        result += r"\begin{array}{c|c|" + "c" * len(self.unbasis) + "}\n"
        result += "     &&" + " & ".join([f"x_{x}" for x in self.unbasis]) + " \\\\\n"
        result += "    \hline\n"
        result += "     z & " + " & ".join([str(x) for x in self.tableau[0]]) + " \\\\\n"
        result += "    \hline\n"
        for i, b in enumerate(self.basis):
            result += f"    x_{b} & " + " & ".join([str(x) for x in self.tableau[i + 1]]) + " \\\\\n"
        result += r"\end{array}"
        
        return result

    
if __name__ == "__main__":
    # 基底変数と非基底変数のインデックス
    basis = [4, 5, 6]
    unbasis = [1, 2, 3]

    # シンプレックス表
    tableau = [
        [0, -1, 4, -7],  # z
        [2, 1, -4, 0],   # x_4
        [3, 0, 1, -2],   # x_5
        [5, -1, 4, -1]   # x_6
    ]

    dictionary = Dictionary(basis, unbasis, tableau)
    dictionary.simplex_method(print_progress=True)
        
        
