package lab1.java;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class AppTest {

    @TempDir
    Path tempDir;

    @Test
    void nullPath_throwsIAE() {
        assertThrows(IllegalArgumentException.class, () -> App.readFile(null));
    }

    @Test
    void emptyPath_throwsIAE() {
        assertThrows(IllegalArgumentException.class, () -> App.readFile("   "));
    }

    @Test
    void nonExisting_throwsNoSuchFile() {
        assertThrows(NoSuchFileException.class, () -> App.readFile("does_not_exist.txt"));
    }

    @Test
    void directoryPath_throwsFileSystemException() throws IOException {
        Path dir = Files.createDirectory(tempDir.resolve("aDir"));
        assertThrows(FileSystemException.class, () -> App.readFile(dir.toString()));
    }

    @Test
    void validFile_readsAllLines() throws IOException {
        Path f = tempDir.resolve("hello.txt");
        Files.write(f, List.of("one", "two", "three"), StandardCharsets.UTF_8, StandardOpenOption.CREATE);
        List<String> lines = App.readFile(f.toString());
        assertEquals(3, lines.size());
        assertEquals("one", lines.get(0));
        assertEquals("three", lines.get(2));
    }
}
