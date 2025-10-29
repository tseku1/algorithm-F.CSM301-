package lab1.java;

import java.io.IOException;
import java.nio.charset.MalformedInputException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

public class App {

    public static List<String> readFile(String path) throws IOException {
        try {
             if (path == null || path.trim().isEmpty()) {
                throw new IllegalArgumentException("failiin zam hooson baina.");
            }

            Path p = Paths.get(path);

            if (!Files.exists(p)) {
                throw new NoSuchFileException("fail oldsongvi: " + p.toAbsolutePath());
            }

            if (Files.isDirectory(p)) {
                throw new FileSystemException("zaasan zam ni file bish (hawtas baina): " + p.toAbsolutePath());
            }

            if (!Files.isReadable(p)) {
                throw new AccessDeniedException("file iig unshih zowshoorol alga: " + p.toAbsolutePath());
            }
            
            return Files.readAllLines(p, StandardCharsets.UTF_8);
        } catch (MalformedInputException mie) {
            MalformedInputException wrapped = new MalformedInputException(mie.getInputLength());
            wrapped.initCause(mie);
            throw new MalformedInputException(mie.getInputLength());
        }
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("ashiglalt: java lab1.App <file iin zam>");
            System.exit(1);
        }

        try {
            List<String> lines = readFile(args[0]);
            System.out.println("amjilttai unshlaa, moriin too: " + lines.size());

            int limit = Math.min(5, lines.size());
            for (int i = 0; i < limit; i++) {
                System.out.println((i + 1) + ": " + lines.get(i));
            }
        } catch (IllegalArgumentException e) {
            System.err.println("Input error: " + e.getMessage());
            System.exit(2);
        } catch (NoSuchFileException e) {
            System.err.println("Error: File not found. " + e.getMessage());
            System.exit(3);
        } catch (AccessDeniedException e) {
            System.err.println("Error: No permission to read the file. " + e.getMessage());
            System.exit(5);
        } catch (FileSystemException e) {
            System.err.println("Error: Path is a directory or other file system issue. " + e.getMessage());
            System.exit(4);
        } catch (MalformedInputException e) {
            System.err.println("Error: File contains invalid UTF-8 or corrupted encoding.");
            System.exit(6);
        } catch (IOException e) {
            System.err.println("IO Error: " + e.getMessage());
            System.exit(7);
        }
    }
}