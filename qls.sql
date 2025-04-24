create database vd1

use vd1
CREATE TABLE Tai_khoan (
    Taikhoan VARCHAR(50) PRIMARY KEY,
    Matkhau VARCHAR(100) NOT NULL,
    Role VARCHAR(20),
    Email VARCHAR(100)
);

-- Bảng phim
CREATE TABLE Phim (
    MaPhim VARCHAR(20) PRIMARY KEY,
    TenPhim VARCHAR(255) NOT NULL,
    ThoiLuong INT,
    TheLoai VARCHAR(100)
);

-- Bảng phòng chiếu
CREATE TABLE Phong_chieu (
    SoPhong VARCHAR(20) PRIMARY KEY,
    Ghe INT, 
    TrangThai VARCHAR(50)
);

-- Bảng suất chiếu
CREATE TABLE Suat_chieu (
    MaSuatChieu VARCHAR(20) PRIMARY KEY,
    PhongChieu VARCHAR(20),
    Phim VARCHAR(20),
    ThoiGian DATETIME,
    FOREIGN KEY (PhongChieu) REFERENCES Phong_chieu(SoPhong),
    FOREIGN KEY (Phim) REFERENCES Phim(MaPhim)
);

-- Bảng vé
CREATE TABLE Ve (
    MaVe VARCHAR(20) PRIMARY KEY,
    SoGhe VARCHAR(10),
    MaSuatChieu VARCHAR(20),
	
    FOREIGN KEY (MaSuatChieu) REFERENCES Suat_chieu(MaSuatChieu)
);

-- Bảng hóa đơn
CREATE TABLE Hoa_don (
    MaHoaDon VARCHAR(20) PRIMARY KEY,
    SoLuong INT,
    MaVe VARCHAR(20),
    GiaVe FLOAT,
    FOREIGN KEY (MaVe) REFERENCES Ve(MaVe)
);

Alter table Tai_khoan 
ADD Ho_ten  Varchar(100) 
Alter table Ve 
add constraint uq_hoten unique (Ho_ten)
Alter table Tai_khoan
add constraint fk_hoadon
foreign key (Mahoadon) references Hoa_don(MaHoaDon)
