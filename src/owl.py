import sys


class OwlLang:
    had_error = False

    def runFile(self, path):
        with open(path, "r") as f:
            source = f.readline()
            self.run(source)

    def runPrompt(self):
        while True:
            line = input("> ")
            if len(line) == 0:
                break

            self.run(line)


    def main(self, argv):
        n = len(argv) - 1
        if n > 1:
            print("Usage: owl [script]")
        elif n == 1:
            self.runFile(sys.argv[1])
        else:
            self.runPrompt()


    def run(self, source: str):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        print(tokens)

    @staticmethod
    def error(line: int, message: str):
        OwlLang.report(line, "", message)

    @staticmethod
    def report(line: int, where: str, message: str):
        print(f"[line {line}] Error ${where}: {message}")
        had_error = True



if __name__ == "__main__":
    owl = OwlLang()
    owl.main(sys.argv)
