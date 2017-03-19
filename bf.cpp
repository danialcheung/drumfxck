#include <string>
#include <iostream>
#include <istream>
#include <ostream>
#include <iterator>
#include <vector>
#include <chrono>
#include <thread>

using namespace std;

// Size of memory (wraparound).
const int N = 10000;

// The backspace character.
const char BACK = '~';

// End of input character.
const char END = EOF;

int main(int argc, char** argv) {
  cout.sync_with_stdio(false);

  int delay_ms = 0;
  if (argc > 1) {
    char* dn = argv[1];
    string st(dn);
    try {
      delay_ms = stoi(st);
    } catch (std::invalid_argument) {
      cerr << "Invalid duration." << endl;
      return 1;
    }
    if (delay_ms < 0) delay_ms = 0;
  }

  vector<char> code;
  {
    code.reserve(1024);
    char ch;
    while ((ch = getchar()) != END) {
      if (ch == BACK)
        code.pop_back();
      else
        code.push_back(ch);
    }
  }
  const unsigned int m = code.size();

  vector<int> mem(N);
  int iMem = 0;

  vector<unsigned int> matching(m);
  for (unsigned int i = 0; i < m; i++) {
    switch (code[i]) {
      case '[':
        {
          unsigned int level = 1;
          unsigned int j = i + 1;
          for (; j < m && level > 0; j++) {
            switch (code[j]) {
              case '[': level++; break;
              case ']': level--; break;
              default: break;
            }
          }

          if (level > 0) {
            cerr << "Mismatching parens.";
            return 1;
          }

          j--;

          //cout << i << "::" << j << "- " << endl;
          matching[i] = j;
          matching[j] = i;
        }
        break;
      case ']':
        break;
      default:
        matching[i] = m;
        break;
    }
  }

#if 0
  for (int i = 0; i < m; i++) {
    cout << "[" << i << "] = " << code[i] << " ";
    if (matching[i] == m)
      cout << endl;
    else
      cout << matching[i] << endl;
  }
#endif

  int pc = 0;
  int level = 0;
  while (pc < m) {
    std::this_thread::sleep_for(std::chrono::milliseconds(delay_ms));
    int pc1 = pc + 1;
    cout << code[pc] << " " << pc << " " << iMem << " " << mem[iMem] << " ";
    switch (code[pc]) {
      case '+':
        mem[iMem]++;
        break;
      case '-':
        mem[iMem]--;
        break;
      case '<':
        iMem--;
        if (iMem < 0) iMem = N-1;
        break;
      case '>':
        iMem++;
        if (iMem >= N) iMem = 0;
        break;
      case '[':
        if (mem[iMem] == 0) {
          pc1 = matching[pc] + 1;
          cout << "- ";
        } else {
          cout << "+ ";
          level++;
        }
        cout << level;
        break;
      case ']':
        pc1 = matching[pc];
        cout << pc1 << " ";
        level--;
        cout << level;
        break;
      case '.':
        {
          char cho = !(((char)mem[iMem]) & (char)0x80) ? (char)mem[iMem] : '*';
          cerr << cho;
          cerr.flush();
          cout << cho;
        }
        break;
      case ',':
        char c; cin >> c;
        mem[iMem] = c;
        break;
      default: break;
    }
    cout << endl;
    pc = pc1;
  }
}
