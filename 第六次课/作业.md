# 第六次课后作业

> 张祎维 计71 2017013640

### 1. 计算样例

- `Virtual Address 6653`

  没有合法物理地址

  ```
  pde index: 0x19
  pde contents: 0x7f
  pte index: 0x12
  ```

- `Virtual Address 1c13`

  有合法物理地址

  ```
  pde index: 0x07
  pde contents: 0xbd
  pte index: 0x00
  pte contents: 0xf6
  value: 0x12
  Physical Address: 0xed3
  ```

- `Virtual Address 6890`

  没有合法物理地址

  ```
  pde index: 0x1a
  pde contents: 0x7f
  pte index: 0x04
  ```

- `Virtual Address 0af6`

  有合法物理地址

  ```
  pde index: 0x02
  pde contents: 0xa1
  pte index: 0x17
  pte contents: 0x7f
  value: 0x03
  Disk Sector Address: 0xff6
  ```

- `Virtual Address 1e6f`

  有合法物理地址

  ```
  pde index: 0x07
  pde contents: 0xbd
  pte index: 0x13
  pte contents: 0x16
  value: 0x1c
  Disk Sector Address: 0x2cf
  ```

### 2. translation程序

见`main.cpp`

